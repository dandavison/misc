typedef struct {
    mon_t *m;
    cv_t *c;
    int value;
} sema_t;


sema_t *sema_create(int initval) {
    s = malloc(1 * sizeof(sema_t));
    s->m = mon_create();
    s->c = cv_create(m);
    s->value = initval;
    return s;
}


void sema_down(sema_t, *s) {
    mon_lock(s->m);
    while (s->value == 0)
        cv_wait(s->cv);
    s->value--;
    mon_release(s->m);
}


void sema_up(sema_t * s) {
    int i;
    printf("stack pointer is close to %p\n", &i);

    mon_lock(s->m);
    s->value++;
    cv_signal(s->cv);
    mon_release(s->m);
}
