%define gobuild(o:) %{expand:
  # https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
  %global _dwz_low_mem_die_limit 0
  %ifnarch ppc64
  go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags %{?__golang_extldflags}'" -a -v -x %{?**};
  %else
  go build -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags %{?__golang_extldflags}'" -a -v -x %{?**};
  %endif
}

Name:           rclone
Version:        1.47.0
Release:        1%{?dist}
Summary:        Rsync for cloud storage
License:        MIT
URL:            http://rclone.org/
Source0:        https://github.com/ncw/rclone/archive/v%{version}/%{name}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}


%description
Rclone is a command line program to sync files and directories to and
from various cloud services.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir -p ./_build/src/github.com/ncw/
ln -s $(pwd) ./_build/src/github.com/ncw/rclone
export GOPATH=$(pwd)/_build:%{gopath}
export GOFLAGS=-mod=vendor

%gobuild -o rclone


%install
install -p -D -m 0755 ./rclone %{buildroot}%{_bindir}/rclone
install -p -D -m 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1


%files
%license COPYING
%doc RELEASE.md README.md MANUAL.md
%{_bindir}/rclone
%{_mandir}/man1/rclone.1*


%changelog
* Sat Apr 13 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.47.0-1
- Release 1.47.0 (#1674166)

* Fri Apr 12 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.46.0-1
- Release 1.46.0

* Tue Dec 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.45-1
- Update to version 1.45
- Fix #1659644

* Mon Nov 05 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.44-1
- Update to version 1.44

* Tue Jun 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.42-1
- Update to version 1.42

* Sun Dec 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.39-1
- Update to version 1.39

* Sun Oct 01 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.38-1
- Update to version 1.38

* Fri Jul 28 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.37-2
- Unbundled revision

* Sun Jul 23 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.37-1
- Update to version 1.37

* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.36-2
- Update to Fedora Packaging Guidelines specification

* Sat Mar 25 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.36-1
- Update to version 1.36

* Fri Jan 06 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.35-1
- Update to version 1.35

* Sun Dec 11 2016 Robert-André Mauchin <zebob.m@gmail.com> - 1.34-1
- Initial RPM release

