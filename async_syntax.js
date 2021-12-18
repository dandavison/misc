// --------------------------------------------------------------------------------------------
// callbacks

fetch_something(args, function(first_response) {
    fetch_something_else_based_on_first_response(first_response.data, function(second_response) {
        fetch_something_else_based_on_second_response(second_response.data, function(third_response) {
            finally_process(third_response)
        })
    })
})

// simplified anonymous function syntax
fetch_something(args, (first_response) =>
    fetch_something_else_based_on_first_response(first_response.data, (second_response) =>
        fetch_something_else_based_on_second_response(second_response.data, finally_process)
    )
)

// --------------------------------------------------------------------------------------------
// promises / futures

future_1 = fetch_something(args)
future_2 = future.map(function(value) {fetch_something_else_based_on_first_response(value)})
future_3 = future.map(function(value) {fetch_something_else_based_on_second_response(value)})
finally_process(future_3.value)

// simplified anonymous function syntax
future_1 = fetch_something(args)
future_2 = future.map((value) => fetch_something_else_based_on_first_response(value))
future_3 = future.map((value) => fetch_something_else_based_on_second_response(value))
finally_process(future_3.value)

// further simplification: eliminate unnecessary anonymous functions
future_1 = fetch_something(args)
future_2 = future.map(fetch_something_else_based_on_first_response)
future_3 = future.map(fetch_something_else_based_on_second_response)
finally_process(future_3.value)

// --------------------------------------------------------------------------------------------
// async / await syntax

async function do_everything() {
    tmp_1 = await fetch_something(args)
    tmp_2 = await fetch_something_else_based_on_first_response(tmp_1)
    tmp_3 = await fetch_something_else_based_on_second_response(tmp_2)
    finally_process(tmp_3)
}
