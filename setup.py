from setuptools import find_packages, setup

setup(
    name='uncertain',
    version='0.4.0',
    packages=find_packages(),
    install_requires=['torch==1.10.2', 'scipy', 'pytorch-lightning==1.9.3', 'h5py', 'pandas<2.0.0', 'requests', 'matplotlib',
                      'scikit-learn', 'tqdm'],
    license='MIT',
    classifiers=['Development Status :: 1 - Beta',
                 'License :: OSI Approved :: MIT License',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence'],
)
