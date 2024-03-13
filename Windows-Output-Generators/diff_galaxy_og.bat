@echo off
title Pygafi Output Generator [Original ROM]
echo Please Wait... Make Sure This Is The [1mOriginal ROM[0m.
for /R . %%f in (*.*) do (
    for %%s in ("%%f") do (
        if %%~zs gtr 0 (
            echo | set/p="%%f - " >> output1.txt
            certutil -hashfile "%%f" SHA256 | findstr /V ":" >> output1.txt
        ) else (
            echo [33mAn empty file was found: %%~nxf. Ignored the file.[0m
        )
    )
)
echo [92mAll Done![0m
timeout /t 5
exit
