# shell.nix for setting up development environment for Nixos/Nix
with (import <nixpkgs> {});
  mkShell {
    buildInputs = [
			(pkgs.python3.withPackages (ps: [
				ps.pip
				ps.pandas
				ps.numpy
				ps.sympy
				# Add other packages here
			]))
    ];
			 # shellHook = ''
			 # python3 -m venv .sympy
			 # source .sympy/bin/activate
			 # pip3 install sympy pandas numpy
			 # '';
  }
