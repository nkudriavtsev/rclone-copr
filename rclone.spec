# Generated by go2rpm 1.5.0

# https://github.com/rclone/rclone
%global goipath         github.com/rclone/rclone
Version:                1.58.1

%gometa

%global common_description %{expand:
Rclone is a command line program to sync files and directories to and
from various cloud services.}

# This package uses gold. Tell package-notes implementation about this.
%global _package_note_linker gold

Name:           rclone
Release:        %autorelease
Summary:        Rsync for cloud storage

License:        MIT
URL:            http://rclone.org/
Source0:        %{gosource}

BuildRequires:  golang(bazil.org/fuse)
BuildRequires:  golang(bazil.org/fuse/fs)
BuildRequires:  golang(github.com/a8m/tree)
BuildRequires:  golang(github.com/aalpar/deheap)
BuildRequires:  golang(github.com/abbot/go-http-auth)
BuildRequires:  golang(github.com/anacrolix/dms/dlna)
BuildRequires:  golang(github.com/anacrolix/dms/soap)
BuildRequires:  golang(github.com/anacrolix/dms/ssdp)
BuildRequires:  golang(github.com/anacrolix/dms/upnp)
BuildRequires:  golang(github.com/artyom/mtab)
BuildRequires:  golang(github.com/atotto/clipboard)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/corehandlers)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/defaults)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/endpoints)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires:  golang(github.com/Azure/azure-pipeline-go/pipeline)
BuildRequires:  golang(github.com/Azure/azure-storage-blob-go/azblob)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-ntlmssp)
BuildRequires:  golang(github.com/buengese/sgzip)
BuildRequires:  golang(github.com/colinmarc/hdfs/v2)
BuildRequires:  golang(github.com/coreos/go-semver/semver)
BuildRequires:  golang(github.com/coreos/go-systemd/activation)
BuildRequires:  golang(github.com/coreos/go-systemd/util)
BuildRequires:  golang(github.com/dop251/scsu)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6/dropbox)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6/dropbox/async)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6/dropbox/auth)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6/dropbox/common)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6/dropbox/files)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6/dropbox/sharing)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6/dropbox/team)
BuildRequires:  golang(github.com/dropbox/dropbox-sdk-go-unofficial/v6/dropbox/users)
BuildRequires:  golang(github.com/gabriel-vasile/mimetype)
BuildRequires:  golang(github.com/go-chi/chi/v5)
BuildRequires:  golang(github.com/go-chi/chi/v5/middleware)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/hanwen/go-fuse/v2/fs)
BuildRequires:  golang(github.com/hanwen/go-fuse/v2/fuse)
BuildRequires:  golang(github.com/iguanesolutions/go-systemd/v5)
BuildRequires:  golang(github.com/iguanesolutions/go-systemd/v5/journald)
BuildRequires:  golang(github.com/iguanesolutions/go-systemd/v5/notify)
BuildRequires:  golang(github.com/jcmturner/gokrb5/v8/client)
BuildRequires:  golang(github.com/jcmturner/gokrb5/v8/config)
BuildRequires:  golang(github.com/jcmturner/gokrb5/v8/credentials)
BuildRequires:  golang(github.com/jlaffaye/ftp)
BuildRequires:  golang(github.com/jzelinskie/whirlpool)
BuildRequires:  golang(github.com/klauspost/compress/huff0)
BuildRequires:  golang(github.com/koofr/go-httpclient)
BuildRequires:  golang(github.com/koofr/go-koofrclient)
BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/ncw/go-acd)
BuildRequires:  golang(github.com/ncw/swift/v2)
BuildRequires:  golang(github.com/nsf/termbox-go)
BuildRequires:  golang(github.com/patrickmn/go-cache)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/pkg/sftp)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/putdotio/go-putio)
BuildRequires:  golang(github.com/rfjakob/eme)
BuildRequires:  golang(github.com/shirou/gopsutil/v3/host)
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
BuildRequires:  golang(github.com/yunify/qingstor-sdk-go/v3/config)
BuildRequires:  golang(github.com/yunify/qingstor-sdk-go/v3/request/errors)
BuildRequires:  golang(github.com/yunify/qingstor-sdk-go/v3/service)
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(goftp.io/server/core)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/crypto/openpgp)
BuildRequires:  golang(golang.org/x/crypto/openpgp/clearsign)
BuildRequires:  golang(golang.org/x/crypto/scrypt)
BuildRequires:  golang(golang.org/x/crypto/ssh)
BuildRequires:  golang(golang.org/x/crypto/ssh/knownhosts)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/ipv4)
BuildRequires:  golang(golang.org/x/net/ipv6)
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
BuildRequires:  golang(storj.io/uplink)

%description
%{common_description}

%prep
%goprep
sed -i "s|github.com/putdotio/go-putio/putio|github.com/putdotio/go-putio|" $(find . -name "*.go")

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
%autochangelog
