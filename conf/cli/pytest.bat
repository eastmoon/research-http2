@rem ------------------- batch setting -------------------
@echo off

@rem ------------------- declare variable -------------------

@rem ------------------- execute script -------------------
call :%*
goto end

@rem ------------------- declare function -------------------

:action
    @rem build locale converter image
    docker build -t pytest-http2 %CLI_DIRECTORY%\conf\docker\pytest

    @rem create cache
    IF NOT EXIST cache (
        mkdir cache
    )

    @rem execute converter
    set INFRA_DOCKER_NETWORK=%PROJECT_NAME%-network
    docker network create %INFRA_DOCKER_NETWORK%
    docker run -ti --rm ^
        -v %CLI_DIRECTORY%\cache:/data ^
        -v %CLI_DIRECTORY%\src\pytest:/app ^
        --network %INFRA_DOCKER_NETWORK% ^
        --hostname pytester ^
        pytest-http2 bash
    goto end

:args
    goto end

:short
    echo Startup pytest service
    goto end

:help
    echo This is a Command Line Interface with project %PROJECT_NAME%
    echo Startup pytest service
    echo.
    echo Options:
    echo      --help, -h        Show more information with command.
    call %CLI_SHELL_DIRECTORY%\utils\tools.bat command-description %~n0
    goto end

:end
