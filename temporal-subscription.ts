
const ONE_MONTH = 30 * 24 * 60 * 60 * 1000;

enum State {
    FreeTrial,
    Subscribed,
    Renewed,
    Canceled,
}

import * as wf from '@temporalio/workflow';
// Temporal's wf.condition(predicate, timeout) function returns a promise that resolves to true if
// the predicate becomes true before the timeout, otherwise false.
import * as activities from 'activities';

var state = State.FreeTrial;

async function subscriptionWorkflow(): Promise<void> {

    wf.setSignalHandler("subscribe", () => state = State.Subscribed)
    wf.setSignalHandler("cancel", () => state = State.Canceled)

    // New user in FreeTrial state
    await activities.callStratoColumn("sendThanksForJoiningMessage", "execute")        
    await wf.condition(() => state !== State.FreeTrial, ONE_MONTH)

    if (state == State.Canceled) {
        await activities.callStratoColumn("sendSorryToSeeYouGoMessage", "execute")        
        await wf.condition(() => state == State.Subscribed)
    }

    // User enters subscription cycle
    while (true) {
        state = State.Canceled
        const subscribeEventReceivedBeforeTimeout = await wf.condition(() => state !== State.Canceled, ONE_MONTH)
        if (!subscribeEventReceivedBeforeTimeout) {
            // They have let their subscription expire and are in Canceled state
            await activities.callStratoColumn("sendSorryToSeeYouGoMessage", "execute")        
            await wf.condition(() => state == State.Subscribed)
        }
        await activities.callStratoColumn("sendThanksForResubscribingMessage", "execute")        
    }
}











    // // Possible states: Subscribed
    // while (true) {
    //     state = State.Canceled
    //     if (await wf.condition(() => state !== State.Canceled, ONE_MONTH)) {
    //         // A subscribe event came in before one month was up
    //         await activities.callStratoColumn("sendThanksForResubscribingMessage", "execute")
    //         continue
    //     } else {
    //         // One month passed with no event. They are in Canceled state.
    //         await wf.condition(() => state == State.Subscribed)
    //     }
    // }








async function subscriptionWorkflow(): Promise<void> {

    wf.setSignalHandler("subscribe", () => state = State.Subscribed)
    wf.setSignalHandler("renew", () => state = State.Renewed)
    wf.setSignalHandler("cancel", () => state = State.Canceled)

    // Free Trial: Race between timeout and subscribe
    await wf.condition(() => state !== State.FreeTrial, ONE_MONTH)

    // Possible states: Subscribed, Canceled
    if (state == State.Canceled) {
        await wf.condition(() => state == State.Subscribed)
    }

    // Possible states: Subscribed
    while (true) {
        if (await wf.condition(() => state in (State.Renewed, State.Subscribed), ONE_MONTH)) {
            state = State.Subscribed
            // A subscribe event came in before one month was up
            await activities.callStratoColumn("sendThanksForResubscribingMessage", "execute")
        }
        else {
            state = State.Canceled
            await wf.condition(() => state == State.Subscribed)
        }
    }
}































enum State2 {
    FreeTrial,
    FreeTrialExpired,
    Subscribed,
    SubscriptionExpired,
  }
  
  

async function subscriptionWorkflow3(): Promise<void> {

    wf.setSignalHandler("subscribe", () => state = State.Subscribed)
    wf.setSignalHandler("cancel", () => wf.cancelWorkflow())

    // Free trial period
    if (!await wf.condition(() => state !== State.FreeTrial, ONE_MONTH)) {
        // Free trial expired; wait for subscribe or cancel
        state = State.FreeTrialExpired
        await wf.condition(() => state !== State.FreeTrialExpired)
    }
    // Subscribed
    while (true) {
        state = State.SubscriptionExpired
        if (!await wf.condition(() => state !== State.SubscriptionExpired, ONE_MONTH)) {
            // Subscription expired; wait for subscribe or cancel signals
            await wf.condition(() => state !== State.SubscriptionExpired)
        }
    }
}


async function subscriptionWorkflow2(): Promise<void> {
    // Free trial period
    await Promise.race([receiveSubscriptionSignal(), receiveCancellationSignal(), sleep(ONE_MONTH)])

    if (state === State.FreeTrialExpired) {
        await Promise.race([receiveSubscriptionSignal(), receiveCancellationSignal()])
    }
    if (state === State.Unsubscribed) {
        return
    }

    // Subscribed
    while (true) {
        state = State.SubscriptionExpired
        await Promise.race([receiveRenewalSignal(), receiveCancellationSignal(), sleep(ONE_MONTH)])
        if (state === State.SubscriptionExpired) {
            await Promise.race([receiveSubscriptionSignal(), receiveCancellationSignal()])
        }
        if (state === State.Unsubscribed) {
            return
        }
    }
}

async function subscriptionWorkflow1(): Promise<void> {

  const stateQuery = wf.defineQuery("state")
  const subscribeSignal = wf.defineSignal("subscribe")
  const renewSignal = wf.defineSignal("renew")
  const cancelSignal = wf.defineSignal("cancel")

  var state = State.FreeTrial;

  wf.setHandler(stateQuery, () => state)
  wf.setHandler(subscribeSignal, () => state = State.Subscribed)
  wf.setHandler(renewSignal, () => state = State.Subscribed)
  wf.setHandler(cancelSignal, () => state = State.Unsubscribed)

  // Free Trial
  await wf.condition(() => state === State.Subscribed, ONE_MONTH)

  // Possible states: FreeTrial, Subscribed, Unsubscribed

  if (state === State.FreeTrial) {
    state = State.FreeTrialExpired
    // Wait for cancellation or subscription
    await wf.condition(() => state !== State.FreeTrialExpired)
  }

  // Possible states: Subscribed, Unsubscribed
  if (state === State.Unsubscribed) {
    return
  }

  // Subscribed
  while (true) {
    if (await wf.condition(() => state !== State.Subscribed, ONE_MONTH)) {
      if (state === State.Unsubscribed) {
        return
      } else {

      }
      
    }
    
  }



  var state = await freeTrial();
  if (state === State.Subscribed) {
    state = await subscription();
  }

  async function receiveSubscribeEvent(): Promise<State> {
    await 
  }

  await Promise.race([awaitSubscribeSignal])

}

async function freeTrial(): Promise<State> {
  var state = State.FreeTrial;

}

async function subscription(): Promise<State> {
  var state = State.Subscribed;

}