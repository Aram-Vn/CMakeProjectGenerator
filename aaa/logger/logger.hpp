
#pragma once

#undef log

#define LOG_LEVEL_DEBUG 0
#define LOG_LEVEL_INFO  1
#define LOG_LEVEL_WARN  2
#define LOG_LEVEL_ERROR 3

// Default to INFO if not defined by compiler flags
#ifndef LOG_LEVEL_THRESHOLD
#define LOG_LEVEL_THRESHOLD 0
#endif

#ifdef _WIN32
#include <windows.h>

static auto _ = []
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    if (hOut == INVALID_HANDLE_VALUE)
        return 0;

    DWORD dwMode = 0;
    if (!GetConsoleMode(hOut, &dwMode))
        return 0;

    dwMode |= ENABLE_VIRTUAL_TERMINAL_PROCESSING;
    SetConsoleMode(hOut, dwMode);
    return 0;
}();
#endif

#define COLOR(x) x
#define RED      COLOR("[1;31m")
#define YELLOW   COLOR("[1;33m")
#define GREEN    COLOR("[1;32m")
#define BLUE     COLOR("[1;34m")
#define RESET    COLOR("[0m")

#ifdef ENABLE_LOG_MUTEX
#include <mutex>
inline std::mutex log_mutex;
#define LOCK_LOG()           std::lock_guard<std::mutex> lock(log_mutex)
#define IS_LOG_MUTEX_ENABLED 1
#else
#define LOCK_LOG()           (void)0
#define IS_LOG_MUTEX_ENABLED 0
#endif

#if defined(__GNUC__) && !defined(__clang__)
// GNU-style macro with ##__VA_ARGS__
#define log(level, fmt, ...)                                                                                               do                                                                                                                     {                                                                                                                          LOCK_LOG();                                                                                                            const char* lvl_str = (level == LOG_LEVEL_ERROR)  ? "[" RED "ERROR" RESET "]"                                                                : (level == LOG_LEVEL_WARN) ? "[" YELLOW "WARN" RESET "]"                                                              : (level == LOG_LEVEL_INFO) ? "[" GREEN "INFO" RESET "]"                                                                                           : "[" BLUE "DEBUG" RESET "]";                                        if (level == LOG_LEVEL_INFO || level == LOG_LEVEL_DEBUG)                                                               {                                                                                                                          fprintf(stderr, "%s ", lvl_str);                                                                                   }                                                                                                                      else                                                                                                                   {                                                                                                                          fprintf(stderr, "%s %s:%d %s(): ", lvl_str, __FILE__, __LINE__, __func__);                                         }                                                                                                                      fprintf(stderr, fmt, ##__VA_ARGS__);                                                                               } while (0)
#else
// C++ standard-compliant version
#define log(level, ...)                                                                                                    do                                                                                                                     {                                                                                                                          LOCK_LOG();                                                                                                            const char* lvl_str = (level == LOG_LEVEL_ERROR)  ? "[" RED "ERROR" RESET "]"                                                                : (level == LOG_LEVEL_WARN) ? "[" YELLOW "WARN" RESET "]"                                                              : (level == LOG_LEVEL_INFO) ? "[" GREEN "INFO" RESET "]"                                                                                           : "[" BLUE "DEBUG" RESET "]";                                        if (level == LOG_LEVEL_INFO || level == LOG_LEVEL_DEBUG)                                                               {                                                                                                                          fprintf(stderr, "%s ", lvl_str);                                                                                   }                                                                                                                      else                                                                                                                   {                                                                                                                          fprintf(stderr, "%s %s:%d %s(): ", lvl_str, __FILE__, __LINE__, __func__);                                         }                                                                                                                      fprintf(stderr, __VA_ARGS__);                                                                                      } while (0)
#endif

#if LOG_LEVEL_DEBUG >= LOG_LEVEL_THRESHOLD
#define log_debug(...) log(LOG_LEVEL_DEBUG, __VA_ARGS__)
#define log_once_debug(...)                                                                                                do                                                                                                                     {                                                                                                                          static bool _once = false;                                                                                             if (!_once)                                                                                                            {                                                                                                                          _once = true;                                                                                                          log(LOG_LEVEL_DEBUG, __VA_ARGS__);                                                                                 }                                                                                                                  } while (0)
#else
#define log_debug(...) (void)0
#endif

#if LOG_LEVEL_INFO >= LOG_LEVEL_THRESHOLD
#define log_info(...) log(LOG_LEVEL_INFO, __VA_ARGS__)
#define log_once_info(...)                                                                                                 do                                                                                                                     {                                                                                                                          static bool _once = false;                                                                                             if (!_once)                                                                                                            {                                                                                                                          _once = true;                                                                                                          log(LOG_LEVEL_INFO, __VA_ARGS__);                                                                                  }                                                                                                                  } while (0)
#else
#define log_info(...)      (void)0
#define log_once_info(...) (void)0
#endif

#if LOG_LEVEL_WARN >= LOG_LEVEL_THRESHOLD
#define log_warn(...) log(LOG_LEVEL_WARN, __VA_ARGS__)
#define log_once_warn(...)                                                                                                 do                                                                                                                     {                                                                                                                          static bool _once = false;                                                                                             if (!_once)                                                                                                            {                                                                                                                          _once = true;                                                                                                          log(LOG_LEVEL_WARN, __VA_ARGS__);                                                                                  }                                                                                                                  } while (0)
#else
#define log_warn(...) (void)0
#endif

#if LOG_LEVEL_ERROR >= LOG_LEVEL_THRESHOLD
#define log_error(...) log(LOG_LEVEL_ERROR, __VA_ARGS__)
#define log_once_error(...)                                                                                                do                                                                                                                     {                                                                                                                          static bool _once = false;                                                                                             if (!_once)                                                                                                            {                                                                                                                          _once = true;                                                                                                          log(LOG_LEVEL_ERROR, __VA_ARGS__);                                                                                 }                                                                                                                  } while (0)
#else
#define log_error(...) (void)0
#endif
        