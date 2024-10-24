{ pkgs }: {
    deps = [
      pkgs.inetutils
        pkgs.python310
        pkgs.python310Packages.flask
        pkgs.python310Packages.requests
        pkgs.python310Packages.whois
        # Ako certstream nije podržan, izostavi ga
    ];
}
