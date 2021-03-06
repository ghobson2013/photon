%{!?python2_sitelib: %define python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        Incremental is a small library that versions your Python projects.
Name:           python-incremental
Version:        16.10.1
Release:        1%{?dist}
License:        MIT
Group:          Development/Languages/Python
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://pypi.python.org/pypi/incremental
Source0:        incremental-%{version}.tar.gz
%define         sha1 incremental=7ec58968fd367d20856488a8991f3a586c7a8695

BuildRequires:  python2
BuildRequires:  python2-libs
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python2
Requires:       python2-libs

BuildArch:      noarch

%description
Incremental is a small library that versions your Python projects.

%package -n     python3-incremental
Summary:        python-incremental
BuildRequires:  python3-devel
BuildRequires:  python3-libs

Requires:       python3
Requires:       python3-libs
%description -n python3-incremental
Python 3 version.

%prep
%setup -q -n incremental-%{version}

%build
python2 setup.py build
python3 setup.py build


%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python2 setup.py test
python3 setup.py test

%files
%defattr(-,root,root)
%{python2_sitelib}/*

%files -n python3-incremental
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
*   Mon Mar 06 2017 Xiaolin Li <xiaolinl@vmware.com> 16.10.1-1
-   Initial packaging for Photon.