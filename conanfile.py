from conans import ConanFile, tools, MSBuild, VisualStudioBuildEnvironment


class WolfsslConan(ConanFile):
    name = "wolfssl"
    version = "4.1.0"
    license = "GPL-2.0"
    author = "wolfSSL <info@wolfssl.com>"
    url = "https://github.com/sersoftin/wolfssl-conan"
    description = "wolfSSL (formerly CyaSSL) is a small, fast, portable implementation of TLS/SSL for embedded devices to the cloud. wolfSSL supports up to TLS 1.3!"
    topics = ("ssl", "tls", "https")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "visual_studio"


    def source(self):
        url = "https://github.com/wolfSSL/wolfssl/archive/v%s-stable.zip" % self.version
        tools.get(url, sha256='b9f12c4f34b7c0e0919ec40da7da0cec5b40ead08d4c77a4ae26739f1e2afdb7')


    def build(self):
        msbuild = MSBuild(self)
        msbuild.build("wolfssl-%s-stable/wolfssl.sln" % self.version, platforms={"x86":"Win32"},
                      build_type=self.settings.build_type)


    def package(self):
        self.copy("*.h", dst="include", src="wolfssl-%s-stable" % self.version)
        self.copy("*.lib", dst="lib", keep_path=False)


    def package_info(self):
        self.cpp_info.libs = ["wolfssl"]