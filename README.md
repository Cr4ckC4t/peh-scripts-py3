# PEH Scripts (for `python3`)

The [Practical Ethical Hacking course by TheCyberMentor](https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course) includes several scripts that students can either recreate themselves or download from the [official repository](https://github.com/TCM-Course-Resources/Practical-Ethical-Hacking-Resources).

The author does a great job at keeping the course contents up-to-date but also leaves the students place for improvement on some of the scripts. Thus, I am going to put up a few updated versions of scripts. 

The updates are mostly minor fixes regarding performance, error handling and python3 compatibility.

**If you find any problems with the code please do let me know by opening an issue.**

# Contents

|File | Changes|
|---|---|
|[port-scanner.py](port-scanner.py)| 🟢 explicit python3 shebang <br /> 🟢 code wrapped in a `main` function <br /> 🟢 general exception handler <br /> 🟢 using `sys.argv[0]` instead of a hardcoded file name <br /> 🟢 moving the `setdefaulttimeout()` out of the `for` loop (it only needs to be called once *before* creating a socket) <br /> ⚠️ I honestly don't know how the original script could run 65534 ports in few seconds in the video. Unless you add threading or decrease the timeout further (which makes the scanner less reliable) this script is not very fast. In the worst case every closed port will cause a delay of `timeout` seconds.|
|[fuzzer.py](fuzzer.py)| 🟢 explicit python3 shebang <br /> 🟢 more precise error messages to help the user understand what happened <br /> 🟢 *colored output just for fun...* <br /> 🟢 timeout detection (so we don't have to cancel the fuzzer manually) <br /> 🟢 *safe* python3 encoding with `latin1` <br /> 🔵 If the script hangs make sure the script is configured correctly (check IP etc.) and the `vulnserver` is accessible. <br /> 🔵 If the script crashes at 100 bytes you'll receive an error output that should give you a hint about what's wrong. |
|[bof-exploit.py](bof-exploit.py)| 🟢 explicit python3 shebang (already included in the updated course content though) <br /> 🟢 *safe* python3 byte encoding (using `latin1` avoids double bytes for values greater than 0x7f) <br /> 🟢 inline generation of bad characters <br /> 🟢 *colored output just for fun...* <br /> 🔵 There are hundreds of ways this can be rewritten - this is just my own quick and dirty working python3 version. |
