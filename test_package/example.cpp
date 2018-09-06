#include <iostream>


#include "pistache/endpoint.h"


int main() {
    Net::Address addr(Net::Ipv4::any(), Net::Port(9080));

    auto opts = Http::Endpoint::options().threads(1);
    Http::Endpoint server(addr);
    server.init(opts);
    server.setHandler(std::make_shared<HelloHandler>());
    // server.serve();
    server.shutdown();
}
