// synchronous
responseA = fetchFromServiceA()
response_B = fetchFromServiceB(responseA.data)
finallyProcess(responseB.data)
 
responseC = fetchFromServiceC()
responseD = fetchFromServiceD(responseC.data)
finallyProcess(responseD.data)


// explicit threads
function ABfunction() {
    responseA = fetchFromServiceA()
    response_B = fetchFromServiceB(responseA.data)
    finallyProcess(responseB.data)
}
function CDfunction() {
    responseC = fetchFromServiceC()
    responseD = fetchFromServiceD(responseC.data)
    finallyProcess(responseD.data)
}
makeThread(ABfunction).run()
makeThread(CDfunction).run()

// event loop
function runEventLoopUntilAllTasksCompleted(tasks) {
    while (tasks) {
        task = selectTaskWhichCanMakeForwardProgress(tasks)
        task.executeSomeInstructionsUntilWaitingOnIO()
        if task.isComplete() {
            tasks.remove(task)
        }
    }
}
runEventLoopUntilAllTasksCompleted([ABTask, CDTask])


// --------------------------------------------------------------------------------------------
// callbacks

fetchFromServiceA(args, callbackA) // At some point this makes a call to socket.read(), in order
                                   // to read the response. But the socket is in non-blocking mode.
                                   // What happens at this point is a task containing a reference to
                                   // callbackA is added to a task queue.
callbackA = (responseA) =>
   fetchFromServiceB(responseA.data, callbackB) // Now, some time has passed and we are executing the
                                                // task that was added to the task queue. A second
                                                // task is enqueued, this time with a reference to
                                                // callbackB

callbackB = (responseB) => finally_process(responseB)   


fetchFromServiceC(args, callbackC)
callbackD = (responseD) => finally_process(responseD)   
callbackC = (responseC) =>
   fetchFromServiceD(responseC.data, callbackD)


callbackA = function(responseA) {
    fetchFromServiceB(responseA.data, callbackB)
}

callbackB = function(responseB) {
    finally_process(responseB)
}

fetchFromServiceA(data, callbackA)

fetchFromServiceA(data, function(responseA) {
    fetchFromServiceB(responseA.data, function(responseB) {
        finally_process(responseB)
    })
})

// simplified anonymous function syntax
fetch(args, (response_1) =>
    fetch_using_response_1(response_1.data, (response_2) =>
        fetch_using_response_2(response_2.data, finally_process)
    )
)

// --------------------------------------------------------------------------------------------
// promises / futures

future_1 = fetch(args)
future_2 = future.map(function(value) {fetch_using_response_1(value)})
future_3 = future.map(function(value) {fetch_using_response_2(value)})
finally_process(future_3.value)

// simplified anonymous function syntax
future_1 = fetch(args)
future_2 = future.map((value) => fetch_using_response_1(value))
future_3 = future.map((value) => fetch_using_response_2(value))
finally_process(future_3.value)

// further simplification: eliminate unnecessary anonymous functions
future_1 = fetch(args)
future_2 = future.map(fetch_using_response_1)
future_3 = future.map(fetch_using_response_2)
finally_process(future_3.value)

// --------------------------------------------------------------------------------------------
// async / await syntax

async function do_everything() {
    tmp_1 = await fetch(args)
    tmp_2 = await fetch_using_response_1(tmp_1)
    tmp_3 = await fetch_using_response_2(tmp_2)
    finally_process(tmp_3)
}
