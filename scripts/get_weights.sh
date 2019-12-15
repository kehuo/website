#!/usr/bin/env bash
usage="$(basename "$0") [-h] [-a] [-i] -- program to install and deploy the project

where:
    -h  show this help text
    -a  get all weights files
    -e  get weights file by instance name"

MODEL_DIR=$(
    cd "$(dirname "$0")" || {
        echo "Path does not exist: $(dirname "$0")"
        exit 1
    }
    pwd
)
MODEL_DIR=${MODEL_DIR%/*}"/website/blueprints/ml/train/weights/"

mkdir -p "${MODEL_DIR}"

declare -A models
models=([mnist]="https://github.com/LucienZhang/ml/releases/download/v1.0/lenet_mnist.h5"
    [cifar10]="https://github.com/LucienZhang/ml/releases/download/v1.1/lenet_cifar10.h5")

function get_weights() {
    cd "${MODEL_DIR}" || {
        echo "Path does not exist: ${MODEL_DIR}"
        exit 1
    }
    echo "Prepare to get models in $MODEL_DIR"
    if [ "$1" = "ALL" ]; then
        for key in ${!models[*]}; do
            address=${models[$key]}
            file_name=${address##*/}
            echo "Getting model $key"
            wget -q "${address}" -O "${file_name}"
            echo "Model $key got!"
        done
    else
        address=${models[$1]}
        if [ ! "${address}" ]; then
            echo "Cannot find model name $1"
            exit 1
        fi
        file_name=${address##*/}
        echo "Getting model $1"
        wget -q "${address}" -O "${file_name}"
        echo "Model $1 got!"
    fi
    md5sum *\.h5 -c models.md5
}

while getopts ':hai:' option; do
    case "$option" in
    h)
        echo "$usage"
        exit
        ;;
    a)
        get_weights "ALL"
        exit
        ;;
    i)
        get_weights "$OPTARG"
        exit
        ;;
    :)
        echo "$usage"
        exit
        ;;
    \?)
        echo "$usage"
        exit
        ;;
    esac
done
shift $((OPTIND - 1))
echo "$usage"
