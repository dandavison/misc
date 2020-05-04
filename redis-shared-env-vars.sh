__set_env_vars_from_redis () {
    (echo >/dev/tcp/localhost/6379) 2>/dev/null && \
    eval $(redis-cli --raw hgetall env |\
           awk '{i = (NR - 1) % 2; args[i] = $1; if(i == 1) { printf("export %s=%s\n", args[0], args[1]) }}')
}
export PROMPT_COMMAND="${PROMPT_COMMAND:-:}; __set_env_vars_from_redis"

# redis-cli hset env MY_ENV_VAR_SHARED_ACROSS_SHELL_PROCESSES=my_env_var_value
