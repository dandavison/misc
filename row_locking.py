for row in queryset:
    begin_transaction()
    acquire_lock_for(row)
    if row in queryset:
        yield row
        commit_transaction()
    else:
        rollback_transaction()
    release_lock_for(row)
