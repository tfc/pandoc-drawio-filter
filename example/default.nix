{ runCommand
, pandoc
, pandoc-drawio-filter
, texlive
}:
let
  env = {
    nativeBuildInputs = [
      pandoc
      pandoc-drawio-filter
      texlive.combined.scheme-tetex
    ];
  };
in
runCommand "example.pdf" env ''
  cp ${./.}/* .
  pandoc -F pandoc-drawio example.md -o $out
''
