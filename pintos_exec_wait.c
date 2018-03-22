struct wait_status
{
  int ref_cnt;                /* 2=child and parent both alive,1=either child or parent alive,0=child and parent both dead. */
  int exit_code;              /* Child exit code, if dead. */
  struct semaphore dead;      /* 1=child alive, 0=child dead. */
};


/* userprog/process.c */
int
process_wait(tid_t child_tid)
{
  /* Get the wait_status for child C */
  [w] = [w for w in cur->children if w.cid == child_tid];

  /* Down wait_status->dead	 				// If C has upped already, this will return immediately, otherwise we will block until C ups */
  sema_down(w->dead);

  /* Save wait_status->exit_code as a local variable */
  exit_code = w->exit_code;

  /* Free the wait_status struct 				// Why don't we have to check ref_count here? because we know the child is dead */
  free(w);

  /* Return the locally saved exit code */
  return exit_code
}


/* userprog/process.c */
void
process_exit(status)
{
  /* Get the wait status shared with P */
  w = cur->parent;

  /* Set wait_status->exit_code = status */
  w->exit_code = status;

  with_synchronization:
    /* Decrement wait_status->ref_count by 1 */
    w->reference_count--;

    /* If wait_status->ref_count is now 0, free the struct */
    if (w->reference_count  == 0)
      free(w);

  /* Else, P is still alive, so we should up wait_status->dead */
  sema_up(w->dead);

  /* Terminate this thread */

}
