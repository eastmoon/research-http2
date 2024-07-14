@rem ------------------- batch setting -------------------
@echo off

@rem ------------------- declare variable -------------------

@rem ------------------- execute script -------------------
call :%*
goto end

@rem ------------------- declare function -------------------

:action
    set INFRA_DOCKER_NETWORK=%PROJECT_NAME%-network
    docker network create %INFRA_DOCKER_NETWORK%
    docker rm -f http2-nginx-1.24-d
    docker run -d ^
        -p 8081:80 ^
        -v %CLI_DIRECTORY%\src\www:/usr/share/nginx/html ^
        --network %INFRA_DOCKER_NETWORK% ^
        --hostname nginx-1.24-d ^
        --name http2-nginx-1.24-d ^
        nginx:1.24
    docker rm -f http2-nginx-1.24
    docker run -d ^
        -v %CLI_DIRECTORY%\src\nginx-1.24\conf.d:/etc/nginx/conf.d ^
        -v %CLI_DIRECTORY%\src\www:/usr/share/nginx/html ^
        -p 8082:80 ^
        --network %INFRA_DOCKER_NETWORK% ^
        --hostname nginx-1.24 ^
        --name http2-nginx-1.24 ^
        nginx:1.24
    docker rm -f http2-nginx-1.25
    docker run -d ^
        -v %CLI_DIRECTORY%\src\nginx-1.25\conf.d:/etc/nginx/conf.d ^
        -v %CLI_DIRECTORY%\src\www:/usr/share/nginx/html ^
        -p 8083:80 ^
        --network %INFRA_DOCKER_NETWORK% ^
        --hostname nginx-1.25 ^
        --name http2-nginx-1.25 ^
        nginx:1.25
    goto end

:args
    goto end

:short
    echo Startup multi frontend framework demo server
    goto end

:help
    echo This is a Command Line Interface with project %PROJECT_NAME%
    echo Startup multi frontend framework demo server
    echo.
    echo Options:
    echo      --help, -h        Show more information with command.
    call %CLI_SHELL_DIRECTORY%\utils\tools.bat command-description %~n0
    goto end

:end
