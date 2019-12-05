usage="$(basename "$0") [-h] [-d] [-e] -- program to install and deploy the project

where:
    -h  show this help text
    -d  deploy the project
    -e  deploy development server"

domain="lucien.red"
work_dir="/var/www/"$domain
git_address="https://github.com/LucienZhang/website.git"

function deploy() {
    apt-get update
    # install conda

    mkdir -p $work_dir
    cd $work_dir

}

function develop() {
    sudo apt-get update
    #sudo apt-get upgrade
}

while getopts ':hde' option; do
    case "$option" in
    h)
        echo "$usage"
        exit
        ;;
    d)
        deploy
        exit
        ;;
    e)
        develop
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
