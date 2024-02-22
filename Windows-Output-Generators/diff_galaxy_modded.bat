@echo off
echo Please Wait... Make Sure This Is The Modded ROM.
for /R . %%f in (*.*) do (
    for %%s in ("%%f") do (
        if %%~zs gtr 0 (
            echo | set/p="%%f - " >> output2.txt
            certutil -hashfile "%%f" SHA256 | findstr /V ":" >> output2.txt
        ) else (
            echo An empty file was found: %%~nxf. Ignored the file.
        )
    )
)
color 0A
echo All Done!
timeout /t 5
exit
