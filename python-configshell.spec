# Copyright 2011, Red Hat

%define oname configshell

Name:           python-configshell
License:        AGPLv3
Group:          System Environment/Libraries
Summary:        A framework to implement simple but nice CLIs
Version:        1.99.1.git987b63b
Release:        5%{?dist}
# placeholder URL and source entries
# archive created using:
# git clone git://risingtidesystems.com/configshell.git
# cd configshell
# git archive 987b63b --prefix configshell-%{version}/ | gzip > configshell-%{version}.tar.gz
URL:            http://www.risingtidesystems.com/git/
Source:         %{oname}-%{version}.tar.gz
Patch1:         %{name}-git-version.patch
Patch2:         %{name}-remove-epydoc-dep.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel epydoc python-simpleparse python-urwid
Requires: python-simpleparse python-urwid

%description
A framework to implement simple but nice configuration-oriented
command-line interfaces.

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p1
%patch2 -p1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}
%doc COPYING README

%changelog
* Fri Sep 23 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-5
* Rebuild

* Thu Aug 25 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-4
- Add patch
  - python-configshell-remove-epydoc-dep.patch

* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-3
- Address comments from spec review
  - drop examples/myshell from doc, it hasn't been updated for API change
  - Fully document procedure to generate source .tar.gz
  - Remove "." from summary
  - Remove commented-out spec todos and other cruft

* Mon Aug 1 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-2
- Update to latest git version
- Add urwid builddep

* Tue May 10 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-1
- Initial packaging
