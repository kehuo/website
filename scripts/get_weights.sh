usage="$(basename "$0") [-h] [-a] [-i] -- program to install and deploy the project

where:
    -h  show this help text
    -a  get all weights files
    -e  get weights file by instance name"

MODEL_DIR=$(
    # shellcheck disable=SC2164
    cd "$(dirname "$0")"
    pwd
)
MODEL_DIR=${MODEL_DIR%/*}"/website/blueprints/ml/ml/model_train/models/"

declare -A models
models=([mnist]="https://github.com/LucienZhang/ml/releases/download/v1.0/lenet_mnist.h5" \
[cifar10]="https://github.com/LucienZhang/ml/releases/download/v1.0/lenet_cifar10.h5")

function get_weights {
    # shellcheck disable=SC2164
    cd "$MODEL_DIR"
    echo "Prepare to get models in $MODEL_DIR"
    if [ "$1" = "ALL" ]; then
        # shellcheck disable=SC2116
        for key in $(echo "${!models[*]}")
        do
            # shellcheck disable=SC2125
            address=models[$key]
            file_name=${address##*/}
            echo "Getting model $key"
            echo "$address"
            echo "$file_name"
            echo "Model $key got!"
        done
    else
        # shellcheck disable=SC2125
        address=models[$1]
        file_name=${address##*/}
        echo "Getting model $1"
        echo "$address"
        echo "$file_name"
        echo "Model $1 got!"
    fi
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
