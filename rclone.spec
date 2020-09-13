# Generated by go2rpm
%bcond_without check

# https://github.com/rclone/rclone
%global goipath         github.com/rclone/rclone
Version:                1.53.1

%gometa

%global common_description %{expand:
Rclone is a command line program to sync files and directories to and
from various cloud services.}

%global golicenses      COPYING
%global godocs          docs CONTRIBUTING.md MAINTAINERS.md MANUAL.md\\\
                        README.md RELEASE.md

Name:           rclone
Release:        1%{?dist}
Summary:        Rsync for cloud storage

License:        MIT
URL:            http://rclone.org/
Source0:        %{gosource}

BuildRequires:  golang(bazil.org/fuse)
BuildRequires:  golang(bazil.org/fuse/fs)
BuildRequires:  golang(github.com/a8m/tree)
BuildRequires:  golang(github.com/abbot/go-http-auth)
BuildRequires:  golang(github.com/anacrolix/dms/dlna)
BuildRequires:  golang(github.com/anacrolix/dms/soap)
BuildRequires:  golang(github.com/anacrolix/dms/ssdp)
BuildRequires:  golang(github.com/anacrolix/dms/upnp)
BuildRequires:  golang(github.com/anacrolix/dms/upnpav)
BuildRequires:  golang(github.com/atotto/clipboard)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/corehandlers)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/defaults)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/Azure/azure-pipeline-go/pipeline)
BuildRequires:  golang(github.com/Azure/azure-storage-blob-go/azblob)
BuildRequires:  golang(github.com/djherbis/times)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/auth)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/common)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/files)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/sharing)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/team)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/users)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(github.com/jlaffaye/ftp)
BuildRequires:  golang(github.com/jzelinskie/whirlpool)
BuildRequires:  golang(github.com/koofr/go-httpclient)
BuildRequires:  golang(github.com/koofr/go-koofrclient)
BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/ncw/go-acd)
BuildRequires:  golang(github.com/ncw/swift)
BuildRequires:  golang(github.com/nsf/termbox-go)
BuildRequires:  golang(github.com/okzk/sdnotify)
BuildRequires:  golang(github.com/patrickmn/go-cache)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/pkg/sftp)
BuildRequires:  golang(github.com/putdotio/go-putio/putio)
BuildRequires:  golang(github.com/rfjakob/eme)
BuildRequires:  golang(github.com/sevlyar/go-daemon)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/skratchdot/open-golang/open)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/cobra/doc)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/t3rm1n4l/go-mega)
BuildRequires:  golang(github.com/Unknwon/goconfig)
BuildRequires:  golang(github.com/xanzy/ssh-agent)
BuildRequires:  golang(github.com/youmark/pkcs8)
BuildRequires:  golang(github.com/yunify/qingstor-sdk-go/config)
BuildRequires:  golang(github.com/yunify/qingstor-sdk-go/request/errors)
BuildRequires:  golang(github.com/yunify/qingstor-sdk-go/service)
BuildRequires:  golang(github.com/goftp/server)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/crypto/scrypt)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/publicsuffix)
BuildRequires:  golang(golang.org/x/net/webdav)
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/oauth2/jws)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/text/unicode/norm)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/api/drive/v2)
BuildRequires:  golang(google.golang.org/api/drive/v3)
BuildRequires:  golang(google.golang.org/api/googleapi)
BuildRequires:  golang(google.golang.org/api/storage/v1)
BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%prep
%goprep
sed -i "s|github.com/yunify/qingstor-sdk-go/v3|github.com/yunify/qingstor-sdk-go|" $(find . -name "*.go")
sed -i "s|goftp.io/server|github.com/goftp/server|" $(find . -name "*.go")
sed -i "s|github.com/etcd-io/bbolt|go.etcd.io/bbolt|" $(find . -name "*.go")

%build
LDFLAGS="-X github.com/ncw/rclone/fs.Version=v%{version} "
%gobuild -o %{gobuilddir}/bin/rclone %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1

%files
%license COPYING
%doc MAINTAINERS.md MANUAL.html RELEASE.md CONTRIBUTING.md MANUAL.md README.md
%doc docs/
%{_bindir}/rclone
%{_mandir}/man1/rclone.1*

%changelog
* Sun Sep 13 2020 Fedora Nicholas Kudriavtsev - 1.53.1-1
- Update to 1.53.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 26 23:53:19 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.51.0-1
- Update to 1.51.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.50.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 22:22:16 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.50.2-1
- Release 1.50.2 (#1756764)

* Sat Sep 28 13:00:14 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.49.3-1
- Release 1.49.3 (#1747050)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 16:26:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.48.0-1
- Release 1.48.0 (#1720839)

* Sat Apr 13 18:34:07 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.47.0-1
- Release 1.47.0 (#1674166)

* Sat Apr 06 21:17:09 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.46.0-1
- Release 1.46.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.45-1
- Update to version 1.45

* Mon Oct 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.44-1
- Update to version 1.44

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.42-1
- Update to version 1.42

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.41-1
- Update to version 1.41
- Use new Go packaging

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

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

