{
  'variables': {
    'platform': '<(OS)',
  },
  'conditions': [
    # Replace gyp platform with node platform, blech
    ['platform == "mac"', {'variables': {'platform': 'darwin'}}],
    ['platform == "win"', {'variables': {'platform': 'win32'}}],
  ],
  'targets': [
    {
      'target_name': 'openvr',
      'defines': [
        'VERSION=0.4.6',
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          "-std=c++11",
          "-stdlib=libc++"
        ],
      },
      'sources': [
        'src/bindings.cpp',
        'src/ivrsystem.cpp',
        'src/ivrcompositor.cpp',
        'src/openvr.cpp'
      ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
        '<(module_root_dir)/node_modules/native-openvr-deps/headers',
      ],
      'conditions': [
        ['OS=="linux"', {
          'library_dirs': ['<(module_root_dir)/node_modules/native-openvr-deps/lib/linux64'],
          'libraries': ['<(module_root_dir)/node_modules/native-openvr-deps/lib/linux64/libopenvr_api.so'],
          'copies':
          [
            {
              'destination': '<(module_root_dir)/build/Release',
              'files': ['<(module_root_dir)/node_modules/native-openvr-deps/bin/linux64/libopenvr_api.so']
            }
          ],
        }],
        ['OS=="mac"', {
          'library_dirs': ['<(module_root_dir)/node_modules/native-openvr-deps/lib/osx32'],
          'libraries': ['libopenvr_api.dylib'],
          'copies':
          [
            {
              'destination': '<(module_root_dir)/build/Release',
              'files': ['<(module_root_dir)/node_modules/native-openvr-deps/bin/osx32/libopenvr_api.dylib']
            }
          ],
        }],
        ['OS=="win"', {
          'library_dirs': ['<(module_root_dir)/node_modules/native-openvr-deps/lib/win64'],
          'libraries': ['openvr_api.lib'],
          'defines' : ['WIN32_LEAN_AND_MEAN', 'VC_EXTRALEAN', 'NOMINMAX'],
          'msvs_settings' : {
            'VCCLCompilerTool' : {
              'AdditionalOptions' : ['/O2','/Oy','/GL','/GF','/Gm-','/EHsc','/MT','/GS','/Gy','/GR-','/Gd']
            },
            'VCLinkerTool' : {
              'AdditionalOptions' : ['/OPT:REF','/OPT:ICF','/LTCG']
            },
          },
          'copies':
          [
            {
              'destination': '<(module_root_dir)/build/Release',
              'files': ['<(module_root_dir)/node_modules/native-openvr-deps/bin/win64/openvr_api.dll']
            }
          ],
        }],
      ],
    }
  ]
}
