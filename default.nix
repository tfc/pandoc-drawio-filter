{ python3Packages, xvfb-run, drawio, doCheck ? false }:

python3Packages.buildPythonApplication rec {
  name = "pandoc-drawio-filter";
  version = "1.0";
  src = ./.;
  propagatedBuildInputs = [
    python3Packages.pandocfilters
    xvfb-run
    drawio
  ];

  # Activate this in a local CI that pins black. Every version difference of
  # this tool can produce failures because of slight changes in the enforced
  # syntax, and then the user can't use the package.
  inherit doCheck;
  checkInputs = [ python3Packages.black ];
  preCheck = ''
    black --check --diff ./**/*.py
  '';
}
