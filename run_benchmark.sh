bin_path=./bin/

function get_ghz() {
  CHECK_OS="$(uname -s)"
  if [[ "$CHECK_OS" == "Darwin"* ]]; then
    echo "ghz_mac"
  elif [[ "$CHECK_OS" == "Linux"* ]]; then
    echo "ghz_linux"
  else
    echo "Not support Window"
    exit -1
  fi
}

function get_bypass_option() {
  json_file=$1
  json_key=$2
  option_name=$3
  value="$(jq $json_key $json_file)"
  if [ $value != "null" ]; then
    echo " $option_name $value"
  fi
}


function get_num_to_seconds_option() {
  json_file=$1
  json_key=$2
  option_name=$3
  value="$(jq $json_key $json_file)"
  if [ "$value" != "null" ]; then
    echo " $option_name ${value}s"
  fi
}

function get_data_option() {
  json_file=$1
  json_key=$2
  option_name=$3
  value="$(jq $json_key $json_file)"
  if [ "$value" != "null" ]; then
    echo " $option_name '$value'"
  fi
}

function get_bool_option() {
  json_file=$1
  json_key=$2
  option_name=$3
  value="$(jq $json_key $json_file)"
  if [[ $value != "null" && $value ]]; then
    echo " $option_name"
  fi
}

function get_options() {
  json_file=$1
  options=""

  options="${options}$(get_bypass_option $json_file ".rps" "--rps")"
  options="${options}$(get_bypass_option $json_file ".total" "-n")"
  options="${options}$(get_bypass_option $json_file ".connections" "--connections")"
  options="${options}$(get_bool_option $json_file ".insecure" "--insecure")"
  options="${options}$(get_bool_option $json_file ".async" "--async")"
  options="${options}$(get_bypass_option $json_file ".proto" "--proto")"
  options="${options}$(get_bypass_option $json_file ".call" "--call")"
  options="${options}$(get_data_option $json_file ".data" "-d")"
  options="${options}$(get_num_to_seconds_option $json_file '.["connect-timeout"]' "--connect-timeout")"

  echo $options
}

function get_output_file_path() {
  json_file=$1
  output_dir=$2
  server_type=$3
  date_prefix=$(date "+%Y-%m-%d")
  echo "${output_dir}/${server_type}_rps_$(jq '.rps' $json_file)_${date_prefix}.json"
}

if [ $# -ne 3 ]; then
  echo "Usage: run_benchamrk.sh <server_type> <request_data_path> <output_dir>"
  echo "support request_data key(ghz option)"
  echo "    - rps(--rps)"
  echo "    - total(-n)"
  echo "    - connections(--connections)"
  echo "    - insecure(--insecure)"
  echo "    - async(--async)"
  echo "    - proto(--proto)"
  echo "    - call(--call)"
  echo "    - data(-d)"
  echo "    - connect-timeout(--connect-timeout)"

  exit -1
else
  ghz_file=$(get_ghz)
  server_type=$1
  request_json=$2
  output_dir=$3

  result_file_path=$(get_output_file_path $request_json $output_dir $server_type)

  CMD="$bin_path$ghz_file $(get_options $request_json) 0.0.0.0:50051 -O json -o $result_file_path"
  echo $CMD
  eval $CMD
fi
