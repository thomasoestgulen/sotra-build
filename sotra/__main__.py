'''__main__.py'''

from sotra import setup_parser
from sotra import bridge
from sotra import obs
from sotra import doc


def main():
    parser = setup_parser.parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return
    
    # obs_parser
    if args.command == "obs":
        print(args)
        if args.list:
            obs.obs_to_txt(dest=args.dest,
                           obs=[*args.list])
        if args.cwd:
            current_obs = obs.obs_from_cwd()
            obs.obs_to_txt(dest=args.dest,
                           obs=current_obs)
    
    # archive_parser
    if args.command == "archive":
        if args.cwd:
            this_obs = obs.obs_from_cwd()
            this_date = obs.get_date_from_cwd()
        
        if args.obs is not None and obs.is_obs(args.obs):
            this_obs = args.obs 
        
        if args.date is not None:
            this_date = args.date

        obs.archive(src_dir=args.src,
                    obs=this_obs,
                    date=this_date)
    
    # doc_parser
    if args.command == "doc":
        if args.print:
            print(doc._get_data())
        if args.revisions:
            doc.update_revisions()
    
    # build_parser
    if args.command == "build":
        if args.bro:
            name = ""
            if args.name: 
                name = args.name
            bridge.build(name)
        elif args.name:
            bridge.name(args.name)


if __name__ == "__main__":
    main()
