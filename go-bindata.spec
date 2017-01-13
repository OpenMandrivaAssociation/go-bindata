%global debug_package   %{nil}
%global import_path     github.com/jteeuwen/go-bindata
%global commit          a0ff2567cfb70903282db057e799fd826784d41d
%global shortcommit     %(c=%{commit}; echo ${c:0:8})

Name:           go-bindata
Version:        3.0.7
Release:        0.git%{shortcommit}.2
Summary:        A small utility which generates Go code from any file
License:        MIT
URL:            http://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/go-bindata-%{shortcommit}.tar.xz
BuildRequires:  golang >= 1.3.3
# git clone https://github.com/jteeuwen/go-bindata
# git archive --format=tar --prefix github.com/jteeuwen/go-bindata-$(date +%Y%m%d)/ HEAD | xz -vf > ../go-bindata-$(date +%Y%m%d).tar.xz

%description
%{summary}

This tool converts any file into managable Go source code. Useful for
embedding binary data into a go program. The file data is optionally gzip
compressed before being converted to a raw byte slice.

%prep
%setup -n go-bindata-%{commit}

%build
mkdir -p ./_build/src/github.com/jteeuwen/
ln -s $(pwd) ./_build/src/github.com/jteeuwen/go-bindata
export GOPATH=$(pwd)/_build:%{gopath}
pushd ./go-bindata/
go build .
popd

%install
install -d -p %{buildroot}%{_bindir}
install -m 755 go-bindata/go-bindata %{buildroot}%{_bindir}/go-bindata

%files
%doc LICENSE README.md
%{_bindir}/go-bindata
