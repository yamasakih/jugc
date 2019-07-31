#!/bin/sh

usage_exit() {
        echo "Usage: $0 [-h] [-i input] [-o output] [-n n_jobs]" 1>&2
        exit 1
}

while getopts "hi:o:n:" op
do
    case $op in
        h)  usage_exit
            ;;
        i)  INPUT="$OPTARG"
            ;;
        o)  OUTPUT="$OPTARG"
            ;;
        n)  N_JOBS="$OPTARG"
            ;;
        *)  usage_exit
            ;;
    esac
done

if [ ! "$INPUT" ]; then
    echo "INPUT is not assigned"
    usage_exit
fi

if [ ! "$OUTPUT" ]; then
    echo "OUTPUT is not assigned"
    usage_exit
fi

if [ ! "$N_JOBS" ]; then
    echo "N_JOBS is not assigned"
    usage_exit
fi

JUGDIR=`mktemp -d ./jugdata.XXXXXX`
for i in $(seq 1 ${N_JOBS})
do
    jug execute --will-cite --jugdir ${JUGDIR} ./jugc/subprocess.py \
        -- -i ${INPUT} -o ${OUTPUT} > ${JUGDIR}/.jug$i.out \
        2> ${JUGDIR}/.jug$i.err &
done
wait