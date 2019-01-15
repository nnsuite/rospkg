Name:           python-rospkg
Version:        1.1.4
Release:        0
License:        BSD
Summary:        ROS package library
Url:            http://wiki.ros.org/rosdep
Group:          descriptionevelopment/Languages/Python
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  python-devel
BuildRequires:  python-argparse
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-mock
BuildRequires:  python-PyYAML
Requires:       python-argparse
Requires:       python-PyYAML

%description
Library for retrieving information about ROS packages and stacks.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_bindir}/rosversion
%{python_sitelib}/*

%changelog
