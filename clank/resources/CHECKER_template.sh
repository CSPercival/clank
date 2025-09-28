#!/bin/bash

g++ -o gen gen.cpp      # test generator
g++ -o slow slow.cpp    # Slow solution, generates correct output
g++ -o model model.cpp  # Model solution, generates incorrect output

TEST_AMOUNT=20000
END=$(( $1 + $TEST_AMOUNT ))
for ((i=$1;i<END;i++))  # {1..20000}
do
    echo $i
    ./gen $i > in
    ./model < in > outM
    ./slow < in > outS
    cmp outM outS || break
    
done