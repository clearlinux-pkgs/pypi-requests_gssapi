#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-requests_gssapi
Version  : 1.2.3
Release  : 7
URL      : https://files.pythonhosted.org/packages/91/d8/67b9ad0c416cdc020f6685fb83bcc7a2e2de77864ab0805ca04cee21b55a/requests-gssapi-1.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/91/d8/67b9ad0c416cdc020f6685fb83bcc7a2e2de77864ab0805ca04cee21b55a/requests-gssapi-1.2.3.tar.gz
Summary  : A GSSAPI authentication handler for python-requests
Group    : Development/Tools
License  : ISC
Requires: pypi-requests_gssapi-license = %{version}-%{release}
Requires: pypi-requests_gssapi-python = %{version}-%{release}
Requires: pypi-requests_gssapi-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(gssapi)
BuildRequires : pypi(requests)

%description
===============================================
        
        Requests is an HTTP library, written in Python, for human beings. This library
        adds optional GSSAPI authentication support and supports mutual
        authentication.
        
        It provides a fully backward-compatible shim for the old

%package license
Summary: license components for the pypi-requests_gssapi package.
Group: Default

%description license
license components for the pypi-requests_gssapi package.


%package python
Summary: python components for the pypi-requests_gssapi package.
Group: Default
Requires: pypi-requests_gssapi-python3 = %{version}-%{release}

%description python
python components for the pypi-requests_gssapi package.


%package python3
Summary: python3 components for the pypi-requests_gssapi package.
Group: Default
Requires: python3-core
Provides: pypi(requests_gssapi)
Requires: pypi(gssapi)
Requires: pypi(requests)

%description python3
python3 components for the pypi-requests_gssapi package.


%prep
%setup -q -n requests-gssapi-1.2.3
cd %{_builddir}/requests-gssapi-1.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651254055
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-requests_gssapi
cp %{_builddir}/requests-gssapi-1.2.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-requests_gssapi/c66ec7cd970188e60dc9aed97511c41258312489
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-requests_gssapi/c66ec7cd970188e60dc9aed97511c41258312489

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
