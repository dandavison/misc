# f() {
#     x=99
#     echo $(eval "echo $1")
# }

# f '$x'


f() {
    x=99
    echo "$1"
}

f '$(eval "echo $1")'
