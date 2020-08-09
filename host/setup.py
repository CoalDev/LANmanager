import py2exe
from distutils.core import setup

setup(
    options = {
        "py2exe":{
            "dll_excludes": ['api-ms-win-core-shlwapi-obsolete-l1-1-0.dll','api-ms-win-core-winrt-error-l1-1-0.dll','api-ms-win-core-threadpool-l1-2-0.dll','api-ms-win-core-kernel32-legacy-l1-1-0.dll','api-ms-win-core-sidebyside-l1-1-0.dll','api-ms-win-core-localization-obsolete-l1-2-0.dll','api-ms-win-core-threadpool-legacy-l1-1-0.dll','api-ms-win-core-com-midlproxystub-l1-1-0.dll','api-ms-win-core-delayload-l1-1-1.dll','api-ms-win-core-atoms-l1-1-0.dll','api-ms-win-core-heap-obsolete-l1-1-0.dll','api-ms-win-core-delayload-l1-1-0.dll','api-ms-win-core-psapi-l1-1-0.dll','api-ms-win-core-string-obsolete-l1-1-0.dll','api-ms-win-security-base-l1-1-0.dll','api-ms-win-core-heap-l1-2-0.dll','api-ms-win-core-synch-l1-2-0.dll','api-ms-win-core-sysinfo-l1-2-1.dll','api-ms-win-core-localization-l1-2-1.dll','api-ms-win-core-libraryloader-l1-2-0.dll','api-ms-win-core-heap-l2-1-0.dll','api-ms-win-eventing-provider-l1-1-0.dll','api-ms-win-security-base-l1-2-0.dll','api-ms-win-core-file-l1-2-1.dll','api-ms-win-core-libraryloader-l1-2-1.dll','api-ms-win-core-processthreads-l1-1-2.dll','api-ms-win-core-profile-l1-1-0.dll','api-ms-win-core-string-l2-1-0.dll','api-ms-win-core-errorhandling-l1-1-1.dll','api-ms-win-core-registry-l1-1-0.dll','api-ms-win-core-string-l1-1-0.dll',"MSVCP90.dll", "HID.DLL", "w9xpopen.exe", "MSVFW32.dll", "AVIFIL32.dll", "AVICAP32.dll", "ADVAPI32.dll", "CRYPT32.dll", "WLDAP32.dll"],
        }
    },
    console=['c:/RemoteShell/LANsystemManager/host/host.py']
)