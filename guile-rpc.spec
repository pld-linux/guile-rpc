Summary:	Guile-RPC - Scheme implementation of XDR and ONC RPC
Summary(pl.UTF-8):	Guile-RPC - implementacja XDR i ONC RPC w Scheme
Name:		guile-rpc
Version:	0.4
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/guile-rpc/%{name}-%{version}.tar.gz
# Source0-md5:	457b6ad093d921fe5fedd25694518527
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/guile-rpc/
BuildRequires:	guile-devel >= 5:2.0
BuildRequires:	texinfo
Requires:	guile >= 5:2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Guile-RPC provides a pure Scheme implementation of XDR and ONC RPC
(respectively RFC 4506 and RFC 1831) for GNU Guile 2.0 or later.

%description -l pl.UTF-8
GNU Guile-RPC zawiera napisaną w czystym Scheme implementację XDR oraz
ONC RPC (odpowiednio RFC 4506 oraz 1831) dla interpretera GNU Guile 2.0
i nowszych.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/grpc-compile
%attr(755,root,root) %{_bindir}/grpc-nfs-export
%attr(755,root,root) %{_bindir}/grpc-rpcinfo
%{_datadir}/guile/site/2.0/rpc
%{_datadir}/guile-rpc
%{_infodir}/guile-rpc.info*
