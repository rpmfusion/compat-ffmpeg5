%undefine _package_note_file

%ifarch %{ix86}
# Fails due to asm issue
%global _lto_cflags %{nil}
%endif

# Cuda and others are only available on some arches
%global cuda_arches x86_64

# Disable because of gcc issue
%global _without_lensfun  1
%if 0%{?fedora}
# fedora nv-codec-headers is too new
%global _without_nvenc    1
%endif
%ifnarch i686
%global _with_bs2b        1
#global _with_chromaprint 1
%global _with_ilbc        1
%global _with_rav1e       1
%global _with_rubberband  1
%global _with_smb         1
%global _with_snappy      1
%global _with_twolame     1
%global _with_wavpack     1
%global _with_webp        1
%global _with_zmq         1
%else
%global _without_vulkan   1
%endif
%ifarch x86_64
%global _with_mfx         1
%global _with_svtav1      1
%global _with_vapoursynth 1
%global _with_vmaf        1
%endif


# Disable nvenc when not relevant
%ifnarch %{cuda_arches} aarch64
%global _without_nvenc    1
%endif

Summary:        Digital VCR and streaming server
Name:           compat-ffmpeg5%{?flavor}
Version:        5.1.4
Release:        2%{?dist}
License:        GPLv3+
URL:            http://ffmpeg.org/
Source0:        http://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz
Source1:        https://ffmpeg.org/releases/ffmpeg-%{version}.tar.xz.asc
Source2:        https://ffmpeg.org/ffmpeg-devel.asc

BuildRequires:  alsa-lib-devel
BuildRequires:  AMF-devel
BuildRequires:  bzip2-devel
%{?_with_faac:BuildRequires: faac-devel}
%{?_with_fdk_aac:BuildRequires: fdk-aac-devel}
%{?_with_flite:BuildRequires: flite-devel}
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
%{!?_without_frei0r:BuildRequires: frei0r-devel}
%{?_with_gme:BuildRequires: game-music-emu-devel}
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  gsm-devel
%{?_with_ilbc:BuildRequires: ilbc-devel}
BuildRequires:  lame-devel >= 3.98.3
%{!?_without_jack:BuildRequires: jack-audio-connection-kit-devel}
%{!?_without_jxl:BuildRequires: libjxl-devel}
%{!?_without_ladspa:BuildRequires: ladspa-devel}
%{!?_without_aom:BuildRequires:  libaom-devel}
%{!?_without_dav1d:BuildRequires:  libdav1d-devel}
%{!?_without_ass:BuildRequires:  libass-devel}
%{!?_without_bluray:BuildRequires:  libbluray-devel}
%{?_with_bs2b:BuildRequires: libbs2b-devel}
%{?_with_caca:BuildRequires: libcaca-devel}
%{!?_without_cdio:BuildRequires: libcdio-paranoia-devel}
%{?_with_chromaprint:BuildRequires: libchromaprint-devel}
%{?_with_crystalhd:BuildRequires: libcrystalhd-devel}
%{!?_without_lensfun:BuildRequires: lensfun-devel}
%if 0%{?_with_ieee1394}
BuildRequires:  libavc1394-devel
BuildRequires:  libdc1394-devel
BuildRequires:  libiec61883-devel
%endif
BuildRequires:  libdrm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libGL-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmysofa-devel
BuildRequires:  libopenmpt-devel
%{?_with_placebo:BuildRequires: libplacebo-devel}
BuildRequires:  librsvg2-devel
# Disable rtmp because of rfbz: 6441 & 2399
%{?_with_rtmp:BuildRequires: librtmp-devel}
%{?_with_smb:BuildRequires: libsmbclient-devel}
BuildRequires:  libssh-devel
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
%{?!_without_vaapi:BuildRequires: libva-devel >= 0.31.0}
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
%{?_with_vapoursynth:BuildRequires: vapoursynth-devel}
%{?!_without_vpx:BuildRequires: libvpx-devel >= 1.4.0}
%{?_with_mfx:BuildRequires: pkgconfig(libmfx) >= 1.23-1}
%ifarch %{ix86} x86_64
BuildRequires:  nasm
%endif
%{?_with_webp:BuildRequires: libwebp-devel}
%{?_with_netcdf:BuildRequires: netcdf-devel}
%{!?_without_nvenc:BuildRequires: nv-codec-headers}
%{!?_without_amr:BuildRequires: opencore-amr-devel vo-amrwbenc-devel}
%{?_with_omx:BuildRequires: libomxil-bellagio-devel}
BuildRequires:  libxcb-devel
BuildRequires:  libxml2-devel
%{!?_without_lv2:BuildRequires:  lilv-devel lv2-devel}
%{!?_without_openal:BuildRequires: openal-soft-devel}
%if 0%{!?_without_opencl:1}
BuildRequires:  opencl-headers ocl-icd-devel
%{?fedora:Recommends: opencl-icd}
%endif
%{?_with_opencv:BuildRequires: opencv-devel}
BuildRequires:  openjpeg2-devel
%{!?_without_opus:BuildRequires: opus-devel >= 1.1.3}
%{!?_without_pulse:BuildRequires: pulseaudio-libs-devel}
BuildRequires:  perl(Pod::Man)
%{?_with_rav1e:BuildRequires: pkgconfig(rav1e)}
%{?_with_rubberband:BuildRequires: rubberband-devel}
%{!?_without_tools:BuildRequires: SDL2-devel}
%{?_with_snappy:BuildRequires: snappy-devel}
BuildRequires:  soxr-devel
BuildRequires:  speex-devel
BuildRequires:  pkgconfig(srt)
%{?_with_svtav1:BuildRequires: svt-av1-devel >= 0.9.0}
%{?_with_tesseract:BuildRequires: tesseract-devel}
#BuildRequires:  texi2html
BuildRequires:  texinfo
%{?_with_twolame:BuildRequires: twolame-devel}
%{?_with_vmaf:BuildRequires: libvmaf-devel >= 1.5.2}
%{?_with_wavpack:BuildRequires: wavpack-devel}
%{!?_without_vidstab:BuildRequires:  vid.stab-devel}
%{!?_without_vulkan:BuildRequires:  vulkan-loader-devel pkgconfig(shaderc)}
%{!?_without_x264:BuildRequires: x264-devel >= 0.0.0-0.31}
%{!?_without_x265:BuildRequires: x265-devel}
%{!?_without_xvid:BuildRequires: xvidcore-devel}
%{!?_without_zimg:BuildRequires:  zimg-devel >= 2.7.0}
BuildRequires:  zlib-devel
%{?_with_zmq:BuildRequires: zeromq-devel}
%{!?_without_zvbi:BuildRequires: zvbi-devel}


Conflicts:      libavcodec-free
Conflicts:      libavdevice-free
Conflicts:      libavfilter-free
Conflicts:      libavformat-free
Conflicts:      libavutil-free
Conflicts:      libpostproc-free
Conflicts:      libswresample-free
Conflicts:      libswscale-free
%{?_with_vmaf:Recommends:     vmaf-models}

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        devel
Summary:        Development package for %{name}
Conflicts:      %{name}-free-devel
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}

# Don't use the %%configure macro as this is not an autotool script
%global ff_configure \
./configure \\\
    --prefix=%{_prefix} \\\
    --bindir=%{_bindir} \\\
    --datadir=%{_datadir}/%{name} \\\
    --docdir=%{_docdir}/%{name} \\\
    --incdir=%{_includedir}/%{name} \\\
    --libdir=%{_libdir} \\\
    --mandir=%{_mandir} \\\
    --arch=%{_target_cpu} \\\
    --optflags="%{optflags}" \\\
    --extra-ldflags="%{?__global_ldflags}" \\\
    --extra-cflags="-I%{_includedir}/rav1e" \\\
    --disable-manpages \\\
    %{?progs_suffix:--progs-suffix=%{progs_suffix}} \\\
    %{?build_suffix:--build-suffix=%{build_suffix}} \\\
    %{!?_without_amr:--enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libvo-amrwbenc --enable-version3} \\\
    --enable-bzlib \\\
    %{?_with_chromaprint:--enable-chromaprint} \\\
    %{!?_with_crystalhd:--disable-crystalhd} \\\
    --enable-fontconfig \\\
    %{!?_without_frei0r:--enable-frei0r} \\\
    --enable-gcrypt \\\
    %{?_with_gmp:--enable-gmp --enable-version3} \\\
    --enable-gnutls \\\
    %{!?_without_ladspa:--enable-ladspa} \\\
    %{!?_without_aom:--enable-libaom} \\\
    %{!?_without_dav1d:--enable-libdav1d} \\\
    %{!?_without_ass:--enable-libass} \\\
    %{!?_without_bluray:--enable-libbluray} \\\
    %{?_with_bs2b:--enable-libbs2b} \\\
    %{?_with_caca:--enable-libcaca} \\\
    %{!?_without_cdio:--enable-libcdio} \\\
    %{?_with_ieee1394:--enable-libdc1394 --enable-libiec61883} \\\
    --enable-libdrm \\\
    %{?_with_faac:--enable-libfaac --enable-nonfree} \\\
    %{?_with_fdk_aac:--enable-libfdk-aac --enable-nonfree} \\\
    %{?_with_flite:--enable-libflite} \\\
    %{!?_without_jack:--enable-libjack} \\\
    %{!?_without_jxl:--enable-libjxl} \\\
    --enable-libfreetype \\\
    %{!?_without_fribidi:--enable-libfribidi} \\\
    %{?_with_gme:--enable-libgme} \\\
    --enable-libgsm \\\
    %{?_with_ilbc:--enable-libilbc} \\\
    %{!?_without_lensfun:--enable-liblensfun} \\\
    --enable-libmp3lame \\\
    --enable-libmysofa \\\
    %{?_with_netcdf:--enable-netcdf} \\\
    %{?_with_mmal:--enable-mmal} \\\
    %{!?_without_nvenc:--enable-nvenc} \\\
    %{?_with_omx:--enable-omx} \\\
    %{!?_without_openal:--enable-openal} \\\
    %{!?_without_opencl:--enable-opencl} \\\
    %{?_with_opencv:--enable-libopencv} \\\
    %{!?_without_opengl:--enable-opengl} \\\
    --enable-libopenjpeg \\\
    --enable-libopenmpt \\\
    %{!?_without_opus:--enable-libopus} \\\
    %{!?_without_pulse:--enable-libpulse} \\\
    %{?_with_placebo:--enable-libplacebo} \\\
    --enable-librsvg \\\
    %{?_with_rav1e:--enable-librav1e} \\\
    %{?_with_rtmp:--enable-librtmp} \\\
    %{?_with_rubberband:--enable-librubberband} \\\
    %{?_with_smb:--enable-libsmbclient --enable-version3} \\\
    %{?_with_snappy:--enable-libsnappy} \\\
    --enable-libsoxr \\\
    --enable-libspeex \\\
    --enable-libsrt \\\
    --enable-libssh \\\
    %{?_with_svtav1:--enable-libsvtav1} \\\
    %{?_with_tesseract:--enable-libtesseract} \\\
    --enable-libtheora \\\
    %{?_with_twolame:--enable-libtwolame} \\\
    --enable-libvorbis \\\
    --enable-libv4l2 \\\
    %{!?_without_vidstab:--enable-libvidstab} \\\
    %{?_with_vmaf:--enable-libvmaf --enable-version3} \\\
    %{?_with_vapoursynth:--enable-vapoursynth} \\\
    %{!?_without_vpx:--enable-libvpx} \\\
    %{!?_without_vulkan:--enable-vulkan --enable-libshaderc} \\\
    %{?_with_webp:--enable-libwebp} \\\
    %{!?_without_x264:--enable-libx264} \\\
    %{!?_without_x265:--enable-libx265} \\\
    %{!?_without_xvid:--enable-libxvid} \\\
    --enable-libxml2 \\\
    %{!?_without_zimg:--enable-libzimg} \\\
    %{?_with_zmq:--enable-libzmq} \\\
    %{!?_without_zvbi:--enable-libzvbi} \\\
    %{!?_without_lv2:--enable-lv2} \\\
    --enable-avfilter \\\
    --enable-libmodplug \\\
    --enable-postproc \\\
    --enable-pthreads \\\
    --disable-static \\\
    --enable-shared \\\
    %{!?_without_gpl:--enable-gpl} \\\
    --disable-debug \\\
    --disable-stripping


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n ffmpeg-%{version}

# fix -O3 -g in host_cflags
sed -i "s|check_host_cflags -O3|check_host_cflags %{optflags}|" configure

%build
%{ff_configure}\
    --shlibdir=%{_libdir} \
    --disable-doc \
    --disable-ffmpeg --disable-ffplay --disable-ffprobe \
%ifnarch %{ix86}
    --enable-lto \
%endif
%ifarch %{ix86}
    --cpu=%{_target_cpu} \
%endif
    %{?_with_mfx:--enable-libmfx} \
%ifarch %{ix86} x86_64 %{power64}
    --enable-runtime-cpudetect \
%endif
%ifarch %{power64}
%ifarch ppc64
    --cpu=g5 \
%endif
%ifarch ppc64p7
    --cpu=power7 \
%endif
%ifarch ppc64le
    --cpu=power8 \
%endif
    --enable-pic \
%endif
%ifarch %{arm}
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%endif
%ifarch armv7hl armv7hnl
    --cpu=armv7-a \
    --enable-vfpv3 \
    --enable-thumb \
%endif
%ifarch armv7hl
    --disable-neon \
%endif
%ifarch armv7hnl
    --enable-neon \
%endif
%endif
    || cat ffbuild/config.log

%make_build V=1

%install
%make_install V=1
rm -r %{buildroot}%{_datadir}/%{name}/

%ldconfig_scriptlets

%files
%doc  CREDITS README.md
%license COPYING.*
%{_libdir}/lib*.so.*

%files devel
%doc MAINTAINERS doc/APIchanges doc/*.txt
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so

%changelog
* Thu Jan 18 2024 Leigh Scott <leigh123linux@gmail.com> - 5.1.4-2
- rebuilt

* Tue Jan 09 2024 Leigh Scott <leigh123linux@gmail.com> - 5.1.4-1
- Update to 5.1.4

* Fri Mar 10 2023 Leigh Scott <leigh123linux@gmail.com> - 5.1.2-1
- Initial build

