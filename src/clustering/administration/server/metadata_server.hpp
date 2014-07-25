// Copyright 2010-2014 RethinkDB, all rights reserved.
#ifndef CLUSTERING_ADMINISTRATION_SERVER_METADATA_SERVER_HPP_
#define CLUSTERING_ADMINISTRATION_SERVER_METADATA_SERVER_HPP_

#include "clustering/administration/server/server_metadata.hpp"

/* A `server_metadata_server_t` is responsible for managing a server's name and tags, as
well as its entries in the directory and semilattice metadata. Proxies don't have a
`server_metadata_server_t`. `server_metadata_server_t` will automatically rename itself
to avoid a name conflict. */

class server_metadata_server_t : public home_thread_mixin_t {
public:
    server_metadata_server_t(
        mailbox_manager_t *_mailbox_manager,
        machine_id_t _my_machine_id,
        const name_string_t &_my_initial_name,
        clone_ptr_t<watchable_t<change_tracking_map_t<peer_id_t,
            server_directory_metadata_t> > > _directory_view,
        boost::shared_ptr<semilattice_readwrite_view_t<servers_semilattice_metadata_t> >
            _semilattice_view
        );

    server_directory_metadata_t get_directory_metadata();

    name_string_t get_my_name() {
        if (permanently_removed_cond.is_pulsed()) return name_string_t();
        return my_name;
    }

    signal_t *get_permanently_removed_signal() {
        return &permanently_removed_cond;
    }

private:
    /* `rename_me()` renames the server unconditionally, without checking for conflicts.
    It does not block. The `server_metadata_server_t` calls it internally, and the
    `server_metadata_client_t` also calls it remotely through `rename_mailbox`. */
    void rename_me(const name_string_t &new_name);

    /* `on_rename_request()` is called in response to a rename request over the network
    */
    void on_rename_request(const name_string_t &new_name,
                           mailbox_t<void()>::addr_t ack_addr);

    /* `on_semilattice_change()` checks if we have been deleted and also checks for name
    conflicts. It does not block, but it may call `on_rename()`. */
    void on_semilattice_change();
    
    mailbox_manager_t *mailbox_manager;
    machine_id_t my_machine_id;
    time_t startup_time;
    name_string_t my_name;
    cond_t permanently_removed_cond;
    watchable_variable_t<server_directory_metadata_t> dir_metadata_var;

    clone_ptr_t<watchable_t<change_tracking_map_t<peer_id_t,
        server_directory_metadata_t> > > directory_view;
    boost::shared_ptr<semilattice_readwrite_view_t<servers_semilattice_metadata_t> >
        semilattice_view;

    auto_drainer_t drainer;

    server_directory_metadata_t::rename_mailbox_t rename_mailbox;
    semilattice_readwrite_view_t<servers_semilattice_metadata_t>::subscription_t
        semilattice_subs;
};

#endif /* CLUSTERING_ADMINISTRATION_SERVER_METADATA_SERVER_HPP_ */

