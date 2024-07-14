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
    docker rm -f http2-curl
    docker run -ti --rm ^
        --network %INFRA_DOCKER_NETWORK% ^
        --hostname tester ^
        --name http2-curl ^
        curlimages/curl sh
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
