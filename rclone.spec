%global goipath         github.com/ncw/rclone
Version:                1.41

%global common_description %{expand:
Rclone is a command line program to sync files and directories to and 
from various cloud services.}

%gometa

Name:           rclone
Release:        1%{?dist}
Summary:        Rsync for cloud storage
License:        MIT
URL:            http://rclone.org/
Source0:        %{gosource}

BuildRequires: golang(bazil.org/fuse)
BuildRequires: golang(bazil.org/fuse/fs)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/storage)
BuildRequires: golang(github.com/Unknwon/goconfig)
BuildRequires: golang(github.com/VividCortex/ewma)
BuildRequires: golang(github.com/a8m/tree)
BuildRequires: golang(github.com/abbot/go-http-auth)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/corehandlers)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/defaults)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires: golang(github.com/billziss-gh/cgofuse/fuse)
BuildRequires: golang(github.com/coreos/bbolt)
BuildRequires: golang(github.com/djherbis/times)
BuildRequires: golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox)
BuildRequires: golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/files)
BuildRequires: golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/sharing)
BuildRequires: golang(github.com/dropbox/dropbox-sdk-go-unofficial/dropbox/users)
BuildRequires: golang(github.com/jlaffaye/ftp)
BuildRequires: golang(github.com/ncw/go-acd)
BuildRequires: golang(github.com/ncw/swift)
BuildRequires: golang(github.com/nsf/termbox-go)
BuildRequires: golang(github.com/okzk/sdnotify)
BuildRequires: golang(github.com/patrickmn/go-cache)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/pkg/sftp)
BuildRequires: golang(github.com/rfjakob/eme)
BuildRequires: golang(github.com/sevlyar/go-daemon)
BuildRequires: golang(github.com/skratchdot/open-golang/open)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/cobra/doc)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(github.com/stretchr/testify/require)
BuildRequires: golang(github.com/t3rm1n4l/go-mega)
BuildRequires: golang(github.com/xanzy/ssh-agent)
BuildRequires: golang(github.com/yunify/qingstor-sdk-go/config)
BuildRequires: golang(github.com/yunify/qingstor-sdk-go/request/errors)
BuildRequires: golang(github.com/yunify/qingstor-sdk-go/service)
BuildRequires: golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(golang.org/x/crypto/ssh)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/net/publicsuffix)
BuildRequires: golang(golang.org/x/net/webdav)
BuildRequires: golang(golang.org/x/net/websocket)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/text/unicode/norm)
BuildRequires: golang(golang.org/x/time/rate)
BuildRequires: golang(google.golang.org/api/drive/v3)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/storage/v1)
BuildRequires: golang(google.golang.org/appengine/log)

%description
%{common_description}


%prep
%forgeautosetup
rm -fr vendor


%build  
%gobuildroot
%gobuild -o _bin/rclone %{goipath}


%install
install -Dpm 0755 _bin/rclone %{buildroot}%{_bindir}/rclone
install -Dpm 0644 ./rclone.1 %{buildroot}%{_mandir}/man1/rclone.1


%files
%license COPYING
%doc RELEASE.md README.md MANUAL.md
%{_bindir}/rclone
%{_mandir}/man1/rclone.1*


%changelog
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

