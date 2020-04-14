#ifndef KHTTPD_HTTP_SERVER_H
#define KHTTPD_HTTP_SERVER_H

#include <linux/workqueue.h>
#include <net/sock.h>
#include "bignum.h"

struct http_server_param {
    struct socket *listen_socket;
};
struct khttp_service {
    bool is_stopped;
    struct list_head worker;
};
/* This structure is used as parameter in work routine */
struct khttp {
    struct socket *sock;
    struct list_head list;
    struct work_struct khttp_work;
};

extern int http_server_daemon(void *arg);

#endif