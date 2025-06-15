
#include <iostream>
#include <logger.hpp>
#include <aaa.h>

int main()
{
    my::aaa a{};
    log_debug("YES: %i\n", a.p);
    return 0;
}
        