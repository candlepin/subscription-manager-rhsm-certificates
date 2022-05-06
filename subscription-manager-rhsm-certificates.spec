Name: subscription-manager-rhsm-certificates
Version: 1.29.26
Release: 1%{?dist}
Summary: Certificates required to communicate with a Red Hat Unified Entitlement Platform
URL: https://www.candlepinproject.org/
%if 0%{?suse_version}
Group: Development/Libraries/Python
License: GPL-2.0
%else
License: GPLv2
%endif

# How to create the source tarball:
#
# git clone https://github.com/candlepin/subscription-manager-rhsm-certificates.git
# dnf install tito
# tito build --tag subscription-manager-rhsm-certificates-$VERSION-$RELEASE --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: openssl

%description
This package contains certificates required for communicating with the REST interface
of a Red Hat Unified Entitlement Platform, used for the management of system entitlements
and to receive access to content.

%prep
%setup -q

%build
# Nothing to do for building

%install
%make_install \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir}

%check
make check

%files
%license COPYING
%dir %{_sysconfdir}/rhsm
%dir %{_sysconfdir}/rhsm/ca
%{_sysconfdir}/rhsm/ca/*.pem

%changelog
