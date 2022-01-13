let
  sources = import ./nix/sources.nix { };
  pkgs = import sources.nixpkgs { };
in
rec {
  pandoc-drawio-filter = pkgs.python3Packages.callPackage ./. { doCheck = true; };
  example = pkgs.callPackage ./example { inherit pandoc-drawio-filter; };
}
