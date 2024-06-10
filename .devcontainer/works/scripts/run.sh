#! /bin/bash


dir_path="${HOME}/works/problems"
date="0606"
difficulty="g"


g++ "${dir_path}/${date}/${difficulty}.cpp"
./a.out < "${dir_path}/${date}/${difficulty}.in" |tee "${dir_path}/${date}/${difficulty}.txt"