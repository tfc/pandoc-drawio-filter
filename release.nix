let
  sources = import ./nix/sources.nix { };
  pkgs = import sources.nixpkgs { };
in
rec {
  pandoc-drawio-filter = pkgs.callPackage ./. { doCheck = true; };
  example = pkgs.callPackage ./example { inherit pandoc-drawio-filter; };
}
