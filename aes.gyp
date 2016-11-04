{
  'includes': ['common.gypi'],
  'targets': [
    {
      'target_name': 'gypaes',
      'type': '<(component)'
	  , 'direct_dependent_settings': {
            'include_dirs': [ './' ]
			, 'defines' : ['AES']
			}
    , 'dependencies': [
      ],
      'defines': [
      ],
      #'include_dirs': [
      #	 '..\..\..\BITBUCKET\WebTv\Foundation.Media.Open\include'
      #],
      'sources': [
	  'aes_modes.c'
	, 'aes_ni.c'
	, 'aescrypt.c'
	, 'aeskey.c'
	, 'aestab.c'
	, 'aes.h'
	, 'aes_ni.h'
	, 'aes_via_ace.h'
	, 'aesopt.h'
	, 'aestab.h'
	, 'brg_endian.h'
	, 'brg_types.h'
      ],
      'conditions': [
      ]        
    }
  ]
}

