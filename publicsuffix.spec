%define commit 45a2bf8ef3e22000fbe4bfa5f9252db41d777001
%define shortcommit %(c=%{commit}; echo ${c:0:7})

Summary:	A list of all known public suffixes
Name:		publicsuffix-list
Version:	0
License:	MPLv2.0
Release:	1
Group:		Networking/WWW
URL:		https://publicsuffix.org/
Source0:	https://github.com/publicsuffix/list/archive/%{commit}/%{name}-%{commit}.zip
BuildArch:	noarch

%description
The Public Suffix List is an initiative of Mozilla, but is maintained as
a community resource. It is available for use in any software, but was
originally created to meet the needs of browser manufacturers. It allows 
browsers to, for example:

 *   Avoid privacy-damaging "supercookies" being set for high-level
     domain name suffixes
 *   Highlight the most important part of a domain name in the user
     interface
 *   Accurately sort history entries by site

%files
%{_datadir}/publicsuffix
%doc README.md
%doc LICENSE

#----------------------------------------------------------------------------

%prep
%setup -q -n list-%{commit}

%build
# test syntax only
%make test-syntax

%install
install -dm 0755 %{buildroot}%{_datadir}/publicsuffix/
install -pm 0644 public_suffix_list.dat %{buildroot}%{_datadir}/publicsuffix/

