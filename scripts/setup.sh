usage="$(basename "$0") [-h] [-d] -- program to install and deploy the project

where:
    -h  show this help text
    -d  deploy the project"

function deploy() {
    sudo apt-get update
    sudo apt-get upgrade
}

while getopts ':hd' option; do
    case "$option" in
    h)
        echo "$usage"
        exit
        ;;
    d)
        deploy
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
