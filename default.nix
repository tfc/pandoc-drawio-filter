{ buildPythonApplication
, fetchFromGitHub
, drawio
, pandocfilters
, xvfb-run
, runtimeShell
, writeScriptBin
, lib
, black
, doCheck ? false
}:

let
  wrappedDrawio = writeScriptBin "drawio" ''
    #!${runtimeShell}


    # Electron really wants a configuration directory to not die with:
    # "Error: Failed to get 'appData' path"
    # so we give it some temp dir as XDG_CONFIG_HOME
    tmpdir=$(mktemp -d)

    function cleanup {
      rm -rf "$tmpdir"
    }
    trap cleanup EXIT

    # Drawio needs to run in a virtual X session, because Electron
    # refuses to work and dies with an unhelpful error message otherwise:
    # "The futex facility returned an unexpected error code."
    XDG_CONFIG_HOME="$tmpdir" ${xvfb-run}/bin/xvfb-run ${drawio}/bin/drawio $@
  '';
in

buildPythonApplication {
  pname = "pandoc-drawio-filter";
  version = "1.1";

  src = ./.;

  propagatedBuildInputs = [
    wrappedDrawio
    pandocfilters
  ];

  # Activate this in a local CI that pins black. Every version difference of
  # this tool can produce failures because of slight changes in the enforced
  # syntax, and then the user can't use the package.
  inherit doCheck;
  checkInputs = [ black ];
  preCheck = ''
    black --check --diff ./**/*.py
  '';
}
